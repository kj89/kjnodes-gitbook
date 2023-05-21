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
peers="d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
