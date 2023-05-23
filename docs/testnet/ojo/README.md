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
peers="b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,43c5a820220dfe96810a7582825acb6caeaaf33e@194.61.28.173:26656,c37e444f67af17545393ad16930cd68dc7e3fd08@95.216.7.169:61156,ec003ade1f7c57d822a1be56c838e668b755bee5@94.190.90.38:33656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
