# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:50090

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

**live-peers** (24)
```bash
peers="23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,34d194b6dab0159471a2aa318949f6a4a238d1b8@77.51.200.79:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,1aa11a85ea0ac04d720ddf15b605fd000e262ac1@128.140.60.175:26656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556,2223f5bf494729b9e9fdf6693d116d34e9d29755@141.94.193.28:55756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
