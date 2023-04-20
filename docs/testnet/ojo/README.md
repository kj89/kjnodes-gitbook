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
peers="d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,340f0623e9338a5c93baf2d8a8825718a86d3e8b@195.3.223.196:26656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,9015c79a2ae5a0033f4ee9237a19ea67579e37f8@135.181.57.104:26656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,81d09ca7ba8f30812402f9076aad78e47f0afc7a@184.174.37.152:50656,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,5d9be9cf3d5161e4891b96a956c3c83de6c0ae49@5.78.75.124:26656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,15101a8cead0eadffc1b822f902bed71051e1638@5.166.240.95:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
