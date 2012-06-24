#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Calc-Units
Summary:	Math::Calc::Units - Human-readable unit-aware calculator
Summary(pl):	Math::Calc::Units - kalkulator obs�uguj�cy jednostki
Name:		perl-Math-Calc-Units
Version:	1.02
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Calc::Units is a simple calculator that keeps track of units. It
currently handles combinations of byte sizes and duration only,
although adding any other multiplicative types is easy. Any unknown
type is treated as a unique user type (with some effort to map English
plurals to their singular forms).

The primary intended use is via the ucalc script that prints out all
of the "readable" variants of a value. For example, "3 bytes" will
only produce "3 byte", but "3 byte / sec" produces the original along
with "180 byte / minute", "10.55 kilobyte / hour", etc.

%description -l pl
Math::Calc::Units to prosty kalkulator zachowuj�cy jednostki.
Aktualnie obs�uguje tylko kombinacje rozmiaru w bajtach i czasu, ale
dodanie dowolnych typ�w multiplikatywnych jest proste. Ka�dy nieznany
typ jest traktowany jako unikalny typ u�ytkownika (z pr�b� zamiany
angielskich form mnogich na pojedyncze).

Podstawowy spos�b u�ycia to skrypt ucalc, wypisuj�cy wszystkie 
"czytelne" warianty warto�ci. Na przyk�ad "3 bytes" daje tylko "3
byte", ale "3 byte / sec" daje warto�� oryginaln� oraz "180 byte /
minute", "10.55 kilobyte / hour" itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Math/Calc/Units.pm
%{perl_sitelib}/Math/Calc/Units
%{_mandir}/man3/*
