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
peers="7d6706d7ee674e2b2c38d3eb47d85ec6e376c377@49.12.123.87:56656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,46984fe69d730d18bfc561830b729fb7689aea2b@95.216.14.46:22656,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,5d9be9cf3d5161e4891b96a956c3c83de6c0ae49@5.78.75.124:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,c37e444f67af17545393ad16930cd68dc7e3fd08@95.216.7.169:61156,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,ec003ade1f7c57d822a1be56c838e668b755bee5@94.190.90.38:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
