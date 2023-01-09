# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v4.0.2 | **Wasm**: OFF

[Website](https://stride.zone) | [Discord](https://discord.gg/mzQZ8dAE7u) | [Twitter](https://twitter.com/stride_zone)

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (36)
```bash
peers="2c1f55e905c7425f995947e2d600ca5ac863b8c1@15.235.53.91:13456,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,ef22ceb48d8d7548fab0972a5e4a9cb3c366fc74@65.109.52.178:26656,6a6a70719d44dfdaa74a074f017dc1f1ff23da62@146.59.0.123:6000,af7229930a59c4d1860fd304a6b2d1c269a18fa4@138.201.8.248:51656,1387946c04bceb472113f657f55f670f71709230@65.108.4.188:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.187:26656,d849878a2972dc8a79ae031e37eb977c56b85f49@13.215.125.32:26656,777274fb08ed48a4e027664e2576a8460272e43c@15.235.115.153:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,06c309d890fe6a1e7d2ac0a600ab077d1e793e18@51.195.89.43:10156,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,f0105a60c4fe0f29348f269bd48b48ae29e8e07b@65.144.145.234:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,68f8dd5372e444bef54f94a62f970c6982aeaae7@51.38.52.188:26639,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,87ba7609ae2aae4c048ef83687fc913b8866cc0b@194.163.161.146:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
