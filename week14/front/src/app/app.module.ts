import { BrowserModule } from '@angular/platform-browser';
import { NgModule,ClassProvider } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import {HttpClientModule,HTTP_INTERCEPTORS} from '@angular/common/http';
import {ProviderService} from './shared/services/provider.service';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { TodoComponent } from './todo/todo.component';
import { TodolistComponent } from './todolist/todolist.component';
import { TodotasksComponent } from './todotasks/todotasks.component';
import {AuthInterceptor} from './AuthInterceptor';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    TodoComponent,
    TodolistComponent,
    TodotasksComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
    FormsModule,
  ],
  providers: [ProviderService,
    <ClassProvider> {
       provide: HTTP_INTERCEPTORS,
       useClass: AuthInterceptor,
       multi: true
     }],

  bootstrap: [AppComponent]
})
export class AppModule { }
