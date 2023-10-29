# Oh-my-zsh 

## 1. Windows 

## 安裝必備工具

1. Winget工具install方式如下:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Force

   $PreRelease = $false

   Write-Output 'Fetching Latest Winget CLI Release'
   $_LatestUrl = ((Invoke-WebRequest 'https://api.github.com/repos/microsoft/winget-cli/releases' -UseBasicParsing | ConvertFrom-Json).Where({ $_.prerelease -eq $PreRelease }) | Select-Object -First 1).assets.Where({ $_.name -match '^Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle$' }).browser_download_url

   Write-Output 'Downloading Winget to TEMP folder'
   $InstallerFile = $(Join-Path -Path $env:TEMP  -ChildPath 'Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle')
   [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
   $WebClient = New-Object System.Net.WebClient
   $WebClient.DownloadFile($_LatestUrl, $InstallerFile)

   Write-Output 'Downloading VCLibs'
   $VCLibsPath = $(Join-Path -Path $env:TEMP -ChildPath 'Microsoft.VCLibs.x64.14.00.Desktop.appx')
   $WebClient.DownloadFile('https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx', $VCLibsPath)

   Write-Output 'Fetching Microsoft UI Nuget Package'
   $_UILibsZipPath = Join-Path -Path $env:TEMP -ChildPath 'Microsoft.UI.Xaml.2.7.zip'
   $WebClient.DownloadFile('https://www.nuget.org/api/v2/package/Microsoft.UI.Xaml/2.7.0', $_UILibsZipPath)

   Write-Output 'Extracting Microsoft UI Appx'
   Expand-Archive -Path $_UILibsZipPath -DestinationPath $(Join-Path -Path $env:TEMP -ChildPath 'Microsoft.UI.Xaml.2.7') -Force
   $_UILibsAppxPath = Join-Path -Path $env:TEMP -ChildPath 'Microsoft.UI.Xaml.2.7\tools\AppX\x64\Release\Microsoft.UI.Xaml.2.7.appx'

   Add-AppxPackage $InstallerFile -DependencyPath $_UILibsAppxPath,$VCLibsPath
   ```
2. 安裝Windows Terminal

   ```powershell
   winget install Microsoft.WindowsTerminal --accept-source-agreements
   ```
3. 安裝powershell7

   ```powershell
   winget install Microsoft.PowerShell
   ```
4. 安裝Oh My Posh

   ```powershell
   winget install JanDeDobbeleer.OhMyPosh
   ```

> 自動安裝`<font style="background: #FFcc00; color: red" >`  oh-my-posh.exe `</font>` 主程式，並設定`<font style="background: pink; color :white">` Path`</font>`環境變數

5. 重開powershell 並安裝Oh My posh所需字體

   執行下列命令會直接安裝`<font style="background: #FFcc00; color: red">`CascadiaCode`</font>`!

   ```powershell
   oh-my-posh.exe font install CascadiaCode
   ```

> 這些字體都來自於[Nerd Fonts Repo](https://github.com/ryanoasis/nerd-fonts/)，而且`<font style="background: pink; color :white">`CascadiaCode`</font>`自行裡面有個`<font style="background: pink; color :white">`CaskaydiaCove NF`</font>`包含大量的glyphs(icons)，可以讓你的命令列環境顯示精美圖示!

6. 工具安裝完畢再重啟powershell
7. 調整 Windows Terminal 設定

   請將 **Windows PowerShell**、**PowerShell Core**、**WSL** 的 **外觀** (Appearance) 調整使用 `CaskaydiaCove NF` 字型 (Font face)！

   建議修改 **PowerShell** 的啟動參數，命令列的部分加入 `-NoLogo` 參數：

   ```powershell
   "C:\Program Files\PowerShell\7\pwsh.exe" -NoLogo
   ```
8. 安裝Terminal-icons模組

   ```powershell
   Install-Module -Name Terminal-Icons -Repository PSGallery -Force
   ```
9. 安裝PSReadLine模組

   優化Powershell環境的利器，不過只能在powershell7執行

   ```powershell
   Install-Module PSReadLine -AllowPrerelease -Force
   ```

## 設定好用的powershell命令輸入環境

1. 初始化 `$PROFILE` 啟動設定檔

   ```ps1
   [System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($PROFILE))

   if (-not (Test-Path -Path $PROFILE -PathType Leaf)) {
     New-Item $PROFILE -Force
   }
   ```
2. 啟用 PSReadLine 並啟用超強自動完成功能

   你可以直接將我的 [$PROFILE_PSReadLine.ps1](https://gist.github.com/doggy8088/d3f3925452e2d7b923d01142f755d2ae) 內容加入到 `$PROFILE` 啟動設定檔中！

   ```ps1
   (Invoke-WebRequest -Uri 'https://gist.githubusercontent.com/doggy8088/d3f3925452e2d7b923d01142f755d2ae/raw/aabe600ed2adccb43165228b8c8ced6e88ac9fc0/$PROFILE_PSReadLine.ps1').Content | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
3. 設定各種命令自動完成提示

   你可以直接將我的 [$PROFILE_ArgumentCompleter.ps1](https://gist.github.com/doggy8088/2bf2a46f7e65ae4197b6092df3835f21) 內容加入到 `$PROFILE` 啟動設定檔中！

   ```ps1
   (Invoke-WebRequest -Uri 'https://gist.githubusercontent.com/doggy8088/2bf2a46f7e65ae4197b6092df3835f21/raw/e5e73da6aabaf51ae49c641f5ca409f38f660443/$PROFILE_ArgumentCompleter.ps1').Content | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
4. 加上幾個我自訂的 Cmdlets / Functions 與停用兩個不太實用的 Cmdlet Aliases

   你可以直接將我的 [$PROFILE_Cmdlets_Functions.ps1](https://gist.github.com/doggy8088/553c4548492b63e4ccbe30d843de85f6) 內容加入到 `$PROFILE` 啟動設定檔中！

   ```ps1
   (Invoke-WebRequest -Uri 'https://gist.githubusercontent.com/doggy8088/553c4548492b63e4ccbe30d843de85f6/raw/5b8492883519ffbd74557e26d7eaf73dc2692c23/$PROFILE_Cmdlets_Functions.ps1').Content | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
5. 匯入 [Terminal-Icons](https://github.com/devblackops/Terminal-Icons) 模組

   ```ps1
   'Import-Module -Name Terminal-Icons' | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
6. 啟動 [Oh My Posh](https://github.com/JanDeDobbeleer/oh-my-posh) 的 Shell 環境

   立即啟用 Oh My Posh 的命令列提示 (Prompt)

   ```sh
   oh-my-posh init pwsh | Invoke-Expression
   ```

   啟動後，你就可以透過 `Get-PoshThemes` 快速顯示所有的 [Themes](https://ohmyposh.dev/docs/themes) 樣式，選一個自己喜歡的版本！ 😍

   假設你選擇 `atomicBit` 的話，就可以這樣重新啟動：

   ```ps1
   oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\atomicBit.omp.json"  | Invoke-Expression
   ```

   然後將以下命令加入到 `$PROFILE` 啟動設定檔中

   ```ps1
   'oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\atomicBit.omp.json"  | Invoke-Expression' | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
7. 下載並啟用我自製的 [`will.omp.yml`](https://gist.github.com/doggy8088/5dbf60c03ac752b4d80d00bf8c36d6d3) 設定檔

   立即啟用 Oh My Posh 的命令列提示 (Prompt)

   ```sh
   Invoke-WebRequest -Uri "https://gist.githubusercontent.com/doggy8088/5dbf60c03ac752b4d80d00bf8c36d6d3/raw/94a2b92f4e3e68bc3413e070f399f6f79cd325bf/will.omp.yml" -OutFile "$env:POSH_THEMES_PATH/will.omp.yaml"
   ```

   選擇 `will` 的話，就可以這樣重新啟動：

   ```ps1
   oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\will.omp.yaml"  | Invoke-Expression
   ```

   然後將以下命令加入到 `$PROFILE` 啟動設定檔中

   ```ps1
   'oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\will.omp.yaml"  | Invoke-Expression' | Out-File -LiteralPath $PROFILE -Append -Encoding utf8
   ```
8. 重新啟動 Windows Terminal 或重新載入 `$PROFILE` 啟動設定檔

   你可以使用**點表示法**重新載入 `$PROFILE` 啟動設定檔：

   ```ps1
   . $PROFILE
   ```

### 設定 WSL 下的 Bash 也使用 Oh My Posh 提示

1. [安裝 Oh My Posh 到 Linux](https://ohmyposh.dev/docs/linux)

   ```sh
   sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
   sudo chmod +x /usr/local/bin/oh-my-posh
   ```
2. 下載官方的 Oh My Posh 設定檔

   ```sh
   mkdir ~/.poshthemes
   wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip
   unzip ~/.poshthemes/themes.zip -d ~/.poshthemes
   chmod u+rw ~/.poshthemes/*.omp.*
   rm ~/.poshthemes/themes.zip
   ```
3. 套用命令列提示 (Prompt)

   ```sh
   eval "$(oh-my-posh init bash)"
   ```
4. 下載並啟用我自製的 [`will.omp.yaml`](https://gist.github.com/doggy8088/5dbf60c03ac752b4d80d00bf8c36d6d3) 設定檔

   ```sh
   curl -sSL https://gist.githubusercontent.com/doggy8088/5dbf60c03ac752b4d80d00bf8c36d6d3/raw/94a2b92f4e3e68bc3413e070f399f6f79cd325bf/will.omp.yml -o ~/.poshthemes/will.omp.yaml
   ```
   將啟用命令加入到 `~/.bashrc` 啟動設定檔並自動重新載入設定

   ```sh
   echo 'eval "$(oh-my-posh init bash --config ~/.poshthemes/will.omp.yaml)"' >> ~/.bashrc
   . ~/.bashrc
   ```
