#include <iostream>
#include <SDL2/SDL.h>

#define WIDTH 600
#define HEIGHT 600
#define DELAY 5000

void update();
bool input();
void draw(SDL_Renderer *renderer);

int main() {

    bool running = true;
    SDL_Renderer *renderer;
    SDL_Window *window;

    if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
        std::cout << "Failed to Initalise: " << SDL_GetError() << std::endl;
        return 1;
    }

    // TODO - Create Individually 
    if (SDL_CreateWindowAndRenderer(WIDTH, HEIGHT, 0, &window, &renderer)) {
        return 1;
    }

    while (running) {
        update();
        running = input();
        draw(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}

void update() {

}

bool input() {
    SDL_Event e;
    while (SDL_PollEvent(&e)) {
        if (e.type == SDL_QUIT) {
            return false;
        }
    }
    return true;
}

void draw(SDL_Renderer *renderer) {
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_Rect rect;
    rect.x = 0; rect.y = 0; rect.w = WIDTH; rect.h = HEIGHT;
    SDL_RenderFillRect(renderer, &rect);
    SDL_RenderClear(renderer);
    SDL_Rect r; r.x = 0; r.y = 0; r.w = 50; r.h = 50;
    SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
    SDL_RenderFillRect(renderer, &r);
    SDL_RenderPresent(renderer);
}