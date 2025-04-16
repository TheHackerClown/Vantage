
import { create } from 'zustand';

type LayoutState = {
  heading: string;
  setHeading: (title: string) => void;
};

export const useLayoutStore = create<LayoutState>((set) => ({
  heading: 'Vantage',
  setHeading: (title) => set({ heading: title }),
}));

