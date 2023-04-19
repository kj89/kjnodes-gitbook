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
peers="fb45d68ce227d2bd3b112d26d27341faebc3736e@78.46.61.117:03656,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,9015c79a2ae5a0033f4ee9237a19ea67579e37f8@135.181.57.104:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:17656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,030c769628e3e56928f8fd143ce9bd9ce53dba34@31.220.85.212:46656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
