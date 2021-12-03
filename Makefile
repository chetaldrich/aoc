test:
	cargo build
	cargo test
.PHONY: test

fix:
	cargo clippy --allow-dirty --allow-staged --fix
	cargo fmt --all
.PHONY: fix