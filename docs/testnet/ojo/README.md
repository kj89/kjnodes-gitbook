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

**live-peers** (34)
```bash
peers="91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,c2ed1269cd275202e4d69fdb64e194e59b20f573@185.245.182.152:40656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,7bf4e4a18bf2006f79f50c79903f77d4e2a5a303@65.21.77.175:33307,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,783187fd50077da7a373ad020a37d47f2d87cd9b@164.90.220.252:32656,323d4309091003ea96ec3076b8bf4dc319c71345@109.205.182.137:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,fb10560d2e3aea7948a375dc87140c156a07acc4@195.201.83.242:17656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,3c8b9cf60b33bdd8b41db6d8af1009e91e14afc8@5.78.67.243:26656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:26656,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,8990953ddef8ca936f1fc3bfc57486cacbc956b4@80.254.8.54:50656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,9aeb9250f279c9e288b7db702380e2970a36e248@5.188.118.105:46656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
