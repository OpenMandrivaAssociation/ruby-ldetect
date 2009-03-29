%define rname ldetect
%define name ruby-%{rname}
%define version 0.0.2
%define release %mkrel 6

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


