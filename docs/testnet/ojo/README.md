# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (38)
```bash
peers="dd55e293588003da8cd6cf56a0e6c6cdab1f6e75@65.109.88.254:46656,5af793eef9fcf435520cfb8674b3339f5f03c340@104.248.45.68:24656,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,25edf9d95199a89bb868d40a7bbeb0ca1f940a65@159.223.77.250:28656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,9dc1f555bd37d6840237f32a2cd4d79ba1c80cb5@65.108.227.112:31656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,7bf4e4a18bf2006f79f50c79903f77d4e2a5a303@65.21.77.175:33307,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,28f1ba6a75fcf8e135de0a60f438317a75dc74aa@39.149.44.187:26656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,f4538b599f92e695b26409c0bd7da7e3b32eec4d@95.216.114.212:30656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,4c735cd1a6eda031866beb6ac5440c4a645dee57@45.94.58.246:34656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
