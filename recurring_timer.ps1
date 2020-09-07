$ErrorActionPreference = "Stop"
for (; ; ) {
    try {
        $notificationTitle = "Hai Ajay, Time for a break: " + [DateTime]::Now.ToShortTimeString()

        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
        $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText01)
        
        #Convert to .NET type for XML manipuration
        $toastXml = [xml] $template.GetXml()
        $toastXml.GetElementsByTagName("text").AppendChild($toastXml.CreateTextNode($notificationTitle)) > $null
        
        #Convert back to WinRT type
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml($toastXml.OuterXml)
        
        $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
        $toast.Tag = "PowerShell"
        $toast.Group = "PowerShell"
        $toast.ExpirationTime = [DateTimeOffset]::Now.AddMinutes(1)
        #$toast.SuppressPopup = $true
        $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PowerShell")
        $notifier.Show($toast);
    }
    catch {
        # do something with $_, log it, more likely
    }
   
    # wait for a minute
    Start-Sleep 900
}