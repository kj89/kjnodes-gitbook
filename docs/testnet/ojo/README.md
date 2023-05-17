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
peers="5a4b066bfd61af1dc759bf84920c792983b82aa4@167.235.252.89:26656,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,02f12e71d5150b49c39123e4e979999b1a08e99d@5.9.79.121:62656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,5a4201370808de8fe5926db82767d8be44c9d288@51.222.42.89:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
