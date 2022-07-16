#include "GDE.h"

class MyScene : public GDE::Scene {
    public:
        explicit MyScene(GDE::Engine* _engine, const std::string& _debugName = "SandboxAndroid") : Scene(_engine, _debugName) {

        }

        ~MyScene() {
            
        }
};

int main(int argc, char *argv[]) {
    GDE::Engine e;
    e.onInit(new MyScene(&e));
    e.onRun();
    e.destroy();
    return 0;
}
