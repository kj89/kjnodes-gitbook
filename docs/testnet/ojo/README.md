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
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="43c5a820220dfe96810a7582825acb6caeaaf33e@194.61.28.173:26656,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,e3d56e1538e41115bccdcb0b83a734407d59d2b9@185.219.142.216:50656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,83a0043b2a2bfff38c3725c70f4c0305c760dfef@213.239.207.175:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
