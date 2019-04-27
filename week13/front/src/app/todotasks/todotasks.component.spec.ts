import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TodotasksComponent } from './todotasks.component';

describe('TodotasksComponent', () => {
  let component: TodotasksComponent;
  let fixture: ComponentFixture<TodotasksComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TodotasksComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TodotasksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
