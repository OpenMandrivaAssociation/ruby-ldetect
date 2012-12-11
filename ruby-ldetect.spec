%define rname ldetect
%define name ruby-%{rname}
%define version 0.0.2
%define release %mkrel 9

Summary: Ruby binding for libdetect
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://people.mandriva.com/~pterjan/soft/ruby-ldetect/
Source0: http://people.mandriva.com/~pterjan/soft/ruby-ldetect/download/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8
BuildRequires: ruby-devel, ldetect-devel >= 0.8.0

%description
Ruby/LDetect is a Ruby binding for Mandriva's libdetect.
It allows hardware detection and mapping to known modules.

%prep
%setup -q 

%build
ruby extconf.rb --vendor
make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_vendorarchdir}/*.so
%doc ChangeLog README sample.rb




%changelog
* Thu Oct 01 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.0.2-9mdv2010.0
+ Revision: 452189
- rebuild for new ldetect

* Mon Sep 28 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.0.2-8mdv2010.0
+ Revision: 450499
- rebuild for new ldetect

* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.0.2-7mdv2010.0
+ Revision: 442800
- rebuild

* Sun Mar 29 2009 Pascal Terjan <pterjan@mandriva.org> 0.0.2-6mdv2009.1
+ Revision: 362069
- use vendor dir
- use makeinstall_std

  + Olivier Blin <oblin@mandriva.com>
    - rebuild for new ldetect
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.2-3mdv2008.0
+ Revision: 16631
- Use Development/Ruby group


* Fri Mar 09 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.2-2mdv2007.1
+ Revision: 140230
- Fix URL

* Fri Mar 09 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.2-1mdv2007.1
+ Revision: 139580
- 0.0.2
- use standard macros
- mkel
- Import ruby-ldetect

* Tue Apr 12 2005 Pascal Terjan <pterjan@mandrake.org> 0.0.1-3mdk
- ship sample.rb

* Thu Mar 31 2005 Pascal Terjan <pterjan@mandrake.org> 0.0.1-2mdk
- lib64 fix

* Thu Feb 17 2005 Pascal Terjan <pterjan@mandrake.org> 0.0.1-1mdk 
- first mdk release

