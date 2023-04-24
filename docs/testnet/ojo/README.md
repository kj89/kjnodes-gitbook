# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (30)
```bash
peers="239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,cabd6a59d90f477a4dd04e87543d01f97b9b619e@185.9.144.138:46656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,057e1ebe8aed2c27bcacb0eeb54dee01f3c6eddd@65.108.200.49:8656,f6d6e625759814e157457a5889961e02dba26ba6@65.109.92.240:37096,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
