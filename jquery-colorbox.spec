%define		plugin	colorbox
Summary:	A light-weight, customizable lightbox plugin for jQuery
Name:		jquery-%{plugin}
Version:	1.3.17
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://colorpowered.com/colorbox/latest/#/%{name}-%{version}.zip
# Source0-md5:	14d84697262db2d2002fe3849eeaa335
URL:		http://colorpowered.com/colorbox/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Why you should be using ColorBox:
- Supports photos, grouping, slideshow, ajax, inline, and iframed
  content.
- Lightweight: 10KB of JavaScript.
- Appearance is controlled through CSS so users can restyle the box.
- Behavior settings can be over-written without altering the ColorBox
  javascript file.
- Can be extended with callbacks & event-hooks without altering the
  source files.
- Completely unobtrusive, options are set in the JS and require no
  changes to existing HTML.
- Preloads background images and can preload upcoming images in a
  photo group.
- Written in jQuery plugin format and can be chained with other jQuery
  commands.
- Generates W3C valid XHTML and adds no JS global variables & passes
  JSLint.
- Released under the MIT License.
- Tested In: Firefox 3+, Safari 3+, Opera 9+, Chrome, Internet
  Explorer 6, 7, 8, 9.

%prep
%setup -qc
mv colorbox .colorbox-dist
mv .colorbox-dist/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p colorbox/jquery.colorbox-min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
