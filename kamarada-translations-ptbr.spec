#
# spec file for package kamarada-translations-ptbr
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


Name:           kamarada-translations-ptbr
Version:        13.1
Release:        1
Summary:        Brazilian Portuguese translations to Kamarada
License:        GPL-2.0+
Group:          System/Localization
Source0:        LICENSE
Url:            http://github.com/kamarada/kamarada-translations-ptbr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  amarok-lang
BuildRequires:  apper-lang
BuildRequires:  bluedevil-lang
BuildRequires:  digikam-lang
BuildRequires:  k3b-lang
BuildRequires:  kamoso-lang
BuildRequires:  kipi-plugins-lang
BuildRequires:  ktorrent-lang
BuildRequires:  libpurple-lang
BuildRequires:  libpurple-plugin-skype-lang
BuildRequires:  MozillaFirefox-translations-common
BuildRequires:  skanlite-lang
BuildRequires:  vlc-noX-lang
BuildRequires:  yakuake-lang

Conflicts:      otherproviders(amarok-lang)
Conflicts:      otherproviders(apper-lang)
Conflicts:      otherproviders(bluedevil-lang)
Conflicts:      otherproviders(digikam-lang)
Conflicts:      otherproviders(k3b-lang)
Conflicts:      otherproviders(kamoso-lang)
Conflicts:      otherproviders(kipi-plugins-lang)
Conflicts:      otherproviders(ktorrent-lang)
Conflicts:      otherproviders(libpurple-lang)
Conflicts:      otherproviders(libpurple-plugin-skype-lang)
Conflicts:      otherproviders(MozillaFirefox-translations-common)
Conflicts:      otherproviders(skanlite-lang)
Conflicts:      otherproviders(vlc-noX-lang)
Conflicts:      otherproviders(yakuake-lang)

Provides:       amarok-lang
Provides:       apper-lang
Provides:       bluedevil-lang
Provides:       digikam-lang
Provides:       k3b-lang
Provides:       kamoso-lang
Provides:       kipi-plugins-lang
Provides:       ktorrent-lang
Provides:       libpurple-lang
Provides:       libpurple-plugin-skype-lang
Provides:       MozillaFirefox-translations-common
Provides:       skanlite-lang
Provides:       vlc-noX-lang
Provides:       yakuake-lang

Requires:       bundle-lang-common-pt
Requires:       bundle-lang-kde-pt
Requires:       kde4-l10n-pt_BR
Requires:       kde4-l10n-pt_BR-data
Requires:       libreoffice-l10n-pt-BR
Requires:       libreoffice-thesaurus-pt
Requires:       translation-update-pt_BR
Requires:       yast2-trans-pt_BR


%description
Brazilian Portuguese translations to Kamarada


%prep
cp -a %{SOURCE0} COPYING


%build


%install
files_to_add=""
# From amarok-lang
files_to_add="$files_to_add /usr/share/doc/kde/HTML/pt_BR/amarok/"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/amarok.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/amarok_scriptengine_qscript.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/amarokcollectionscanner_qt.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/amarokpkg.mo"
# From apper-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/apper.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/plasma_package_updater.mo"
# From bluedevil-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/bluedevil.mo"
# From digikam-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/digikam.mo"
# From k3b-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/k3b.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/k3bsetup.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kio_videodvd.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/libk3b.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/libk3bdevice.mo"
# From kamoso-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kamoso.mo"
# From kipi-plugins-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_acquireimages.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_advancedslideshow.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_batchprocessimages.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_calendar.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_dngconverter.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_expoblending.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_facebook.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_flashexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_flickrexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_galleryexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_gpssync.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_htmlexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_imageviewer.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_ipodexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_jpeglossless.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_kioexportimport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_metadataedit.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_picasawebexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_piwigoexport.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_printimages.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_rawconverter.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_removeredeyes.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_sendimages.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_shwup.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_smug.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugin_timeadjust.mo"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/kipiplugins.mo"
# From ktorrent-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/ktorrent.mo"
# From libpurple-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/pidgin.mo"
# From libpurple-plugin-skype-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/skype4pidgin.mo"
# From MozillaFirefox-translations-common
files_to_add="$files_to_add /usr/lib/firefox/browser/extensions/langpack-pt-BR@firefox.mozilla.org/"
# From skanlite-lang
files_to_add="$files_to_add /usr/share/doc/kde/HTML/pt_BR/skanlite"
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/skanlite.mo"
# From vlc-noX-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/vlc.mo"
# From yakuake-lang
files_to_add="$files_to_add /usr/share/locale/pt_BR/LC_MESSAGES/yakuake.mo"


echo "%defattr(-,root,root)" > files.kamarada-translations-ptbr
echo "%doc COPYING" >> files.kamarada-translations-ptbr

for f in $files_to_add; do
  if ! test -L "$f" && test -d "$f"; then
    mkdir -p $RPM_BUILD_ROOT/$f
    cp -R "$f/" "$RPM_BUILD_ROOT/$f/../"
  else
    mkdir -p $RPM_BUILD_ROOT/`dirname "$f"`
    cp -a "$f" "$RPM_BUILD_ROOT/$f"
  fi
  echo "$f" >> files.kamarada-translations-ptbr
done


%files -f files.kamarada-translations-ptbr


%changelog
* Wed Sep 03 2014 kamaradalinux@gmail.com
- Initial draft
