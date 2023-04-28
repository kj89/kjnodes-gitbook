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

**live-peers** (30)
```bash
peers="2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,2691bb6b296b951400d871c8d0bd94a3a1cdbd52@65.109.93.152:33656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,46984fe69d730d18bfc561830b729fb7689aea2b@95.216.14.46:22656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:17656,5d9be9cf3d5161e4891b96a956c3c83de6c0ae49@5.78.75.124:26656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,1aa11a85ea0ac04d720ddf15b605fd000e262ac1@128.140.60.175:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,fb10560d2e3aea7948a375dc87140c156a07acc4@65.109.20.117:17656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
