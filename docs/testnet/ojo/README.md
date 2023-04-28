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
peers="9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,20d9bb13b09c054c30f1b48fbd276aa255af5a34@65.108.238.147:37656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,4e309b79b9147a0243f6e0cbc824f86e10bd09de@65.109.234.254:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
