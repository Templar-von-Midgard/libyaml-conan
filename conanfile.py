from conans import ConanFile, CMake, tools


class LibyamlConan(ConanFile):
    name = 'libyaml'
    version = '0.2.2'
    license = 'MIT'
    author = 'Csonkás Kristóf Gyula csonkas.kristof@gmail.com'
    url = 'https://github.com/Templar-von-Midgard/libyaml-conan'
    description = 'LibYAML is a YAML parser and emitter library.'
    topics = ('yaml',)
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        'shared': [True, False]
    }
    default_options = 'shared=False'
    generators = 'cmake'

    def package_id(self):
        del self.info.settings.compiler

    def source(self):
        git = tools.Git(folder=self.name)
        git.clone('https://github.com/yaml/libyaml.git', branch=self.version)

    def build(self):
        cmake = CMake(self, generator='Ninja')
        cmake.definitions['YAML_STATIC_LIB_NAME'] = 'yaml'
        cmake.configure(source_folder=self.name)
        cmake.build()
        cmake.test()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ['yaml']
