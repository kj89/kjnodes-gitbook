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
peers="2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,9d6ff8ca3c73ab08b7fcd59f47ed9cf7bd80f14e@185.217.126.187:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,fbeb2b37fe139399d7513219e25afd9eb8f81f4f@65.21.170.3:38656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,ec003ade1f7c57d822a1be56c838e668b755bee5@94.190.90.38:33656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,09e190d2605573581fa67ec4b9b55c8995aa9abf@207.244.236.87:50656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,1b70500fde59305c11143a9142529e928574fd71@65.109.112.20:50656,8e2ea63e2ff7ecbe75aef6012c4df050d5e1de0f@65.21.139.155:28656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,cb706ebe1d7a1f1d3e281bf46a78d84251f50810@95.217.58.111:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
