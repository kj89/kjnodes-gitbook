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
peers="ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,fbeb2b37fe139399d7513219e25afd9eb8f81f4f@65.21.170.3:38656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,0c89a312b6fc88661ff78642eb04defd29bd7e9c@65.108.98.124:60466,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
