import { BrowserModule } from '@angular/platform-browser';
import {NgModule, Provider} from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ProviderService} from "./shared/services/provider.service";
import { TaskComponent } from './task/task.component';
import { TasklistComponent } from './tasklist/tasklist.component';
import { TasksComponent } from './tasks/tasks.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    TaskComponent,
    TasklistComponent,
    TasksComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [
    ProviderService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
