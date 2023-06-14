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
peers="17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,fe8c46222c3a013115797176623597aafc16e33a@173.212.203.238:46656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,e54b02d103f1fcf5189a86abe542670979d2029d@65.109.85.170:58656,7d59fd87e149226d58d28846a17711ec8b89888c@65.109.122.105:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,e7aefcb24cfe3e6e27147b4202a6188a1bb76f2d@15.235.10.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
