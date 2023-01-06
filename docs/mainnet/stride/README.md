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
peers="5b193f60f2b8378c42d7d30bd70d45de2b70730e@65.108.202.143:16656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,ef22ceb48d8d7548fab0972a5e4a9cb3c366fc74@65.109.52.178:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,be0522cbc5ea30f14355ff6d05ed4b9cf47d7dda@188.172.228.162:26656,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,741864e5c0bd37ae602c2c853c71a2c3b84589a0@65.21.88.172:29656,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,4040b0b8a983a8073319163c5ab67cb1b0a19d36@185.245.182.112:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,1387946c04bceb472113f657f55f670f71709230@65.108.4.188:12256,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,7ec6917a0519decec00a9a29f599c4d90ebf3b86@65.21.136.170:51656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,60ae01f26f6931341f20d8112660c83eecca154e@194.163.172.115:12256,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,82588f011491c6100d922d133f52fc23460b9231@135.181.67.235:26656,a2128f5552cf4ae60a769999c7fddc5d9d44d149@15.235.42.151:26661"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
