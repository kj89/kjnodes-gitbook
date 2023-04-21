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
peers="3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,a654bbc2b27134da4eb1fcc08f07a2c9ea0deec7@51.79.77.103:12656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,34d194b6dab0159471a2aa318949f6a4a238d1b8@77.51.200.79:50656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,cabd6a59d90f477a4dd04e87543d01f97b9b619e@185.9.144.138:46656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,89265c81649253b409469432b5b38870aa0abe93@37.187.95.179:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
