#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-axiom-types
Version  : 0.1.1
Release  : 5
URL      : https://rubygems.org/downloads/axiom-types-0.1.1.gem
Source0  : https://rubygems.org/downloads/axiom-types-0.1.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# axiom-types
Define types with optional constraints for use within axiom and other libraries.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n axiom-types-0.1.1
gem spec %{SOURCE0} -l --ruby > rubygem-axiom-types.gemspec

%build
gem build rubygem-axiom-types.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
axiom-types-0.1.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/axiom-types-0.1.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.ruby-gemset
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/Gemfile.devtools
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/TODO
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/axiom-types.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/devtools.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/flay.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/flog.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/mutant.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/reek.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/roodi.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/config/yardstick.yml
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom-types.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/array.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/boolean.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/class.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/date.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/date_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/decimal.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/encodable.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/float.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/length_comparable.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/numeric.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/object.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/set.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/string.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/support/infinity.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/support/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/symbol.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/time.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/type.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/value_comparable.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/lib/axiom/types/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/array/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/boolean/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/class_methods/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/collection/class_methods/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/collection/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/encodable/class_methods/extended_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/encodable/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/hash/class_methods/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/hash/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/infinity/coerce_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/infinity/spaceship_operator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/infinity/succ_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/length_comparable/class_methods/extended_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/length_comparable/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/length_comparable/range_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/negative_infinity/spaceship_operator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/object/class_methods/coercion_method_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/object/class_methods/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/object/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/object/class_methods/inspect_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/object/class_methods/primitive_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/options/accept_options_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/options/inherited_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/set/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/anonymous_predicate_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/base_predicate_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/base_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/constraint_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/include_predicate_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/includes_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/infer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/type/class_methods/new_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/value_comparable/class_methods/extended_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/value_comparable/finalize_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/axiom-types-0.1.1/spec/unit/axiom/types/value_comparable/range_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/axiom-types-0.1.1.gemspec
