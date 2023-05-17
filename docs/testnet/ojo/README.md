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

**live-peers** (11)
```bash
peers="d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,9d9d7a060cdf621b275c5127e736ad25f381eb6b@95.214.52.138:25676,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,5a4201370808de8fe5926db82767d8be44c9d288@51.222.42.89:50656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,e73e29131fca25c0aa3da698f76ff708a361f16a@65.109.99.212:16656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
