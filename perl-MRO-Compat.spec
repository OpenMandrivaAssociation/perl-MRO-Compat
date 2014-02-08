%define upstream_name	MRO-Compat
%define upstream_version    0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8
Summary:	mro::* interface compatibility for Perls < 5.9.5
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://search.cpan.org/CPAN/authors/id/B/BL/BLBLACK/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Module::AutoInstall)
BuildRequires:	perl(Class::C3) >= 0.19
BuildRequires:	perl(Class::C3::XS) >= 0.19
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.

This upstream_name provides those interfaces for earlier versions of Perl
(back to 5.6.0 anyways).

It is a harmless no-op to use this upstream_name on 5.9.5+. If you're
writing a piece of software that would like to use the parts of 5.9.5+'s
mro:: interfaces that are supported here, and you want compatibility with
older Perls, this is the upstream_name for you.

Some parts of this interface will work better with Class::C3::XS installed,
but it's not a requirement.

This upstream_name never exports any functions. All calls must be fully
qualified with the mro:: prefix.

The interface documentation here serves only as a quick reference of what
the function basically does, and what differences between MRO::Compat and
5.9.5+ one should look out for. The main docs in 5.9.5's mro are the real
interface docs, and contain a lot of other

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/MRO
%{_mandir}/*/*


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-5mdv2012.0
+ Revision: 767800
- fix stupid and anal rpmlint enforcements that does not even show in the build system output.
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-3
+ Revision: 676884
- rebuild
- mass rebuild

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 384738
- new version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2010.0
+ Revision: 371661
- new version

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 220146
- update to new version 0.09

* Sun May 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.0
+ Revision: 211159
- update to new version 0.07

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2008.1
+ Revision: 97519
- update to new version 0.05

* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.0
+ Revision: 77098
- new version

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
+ Revision: 48108
- import perl-MRO-Compat


* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
- first mdv release 
