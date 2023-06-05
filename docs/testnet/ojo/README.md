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
peers="256000ae8b93e9e29028c904f0b3a763202d1747@85.10.192.146:21656,1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,f616a5d02454f0d80460896a0b7d8dfba8bdbac9@173.249.21.248:26656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
