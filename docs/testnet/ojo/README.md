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
peers="ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,7d59fd87e149226d58d28846a17711ec8b89888c@65.109.122.105:60956,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,e7aefcb24cfe3e6e27147b4202a6188a1bb76f2d@15.235.10.78:26656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,a654bbc2b27134da4eb1fcc08f07a2c9ea0deec7@51.79.77.103:12656,5a4201370808de8fe5926db82767d8be44c9d288@51.222.42.89:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
