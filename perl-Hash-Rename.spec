%define upstream_name    Hash-Rename
%define upstream_version 1.100860

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Rename hash keys
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Using this module you can rename a hash's keys in place.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.860-2mdv2011.0
+ Revision: 655021
- rebuild for updated spec-helper

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528434
- update to 1.100860

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 503864
- update to 0.03

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 502081
- import perl-Hash-Rename


* Mon Feb 08 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
