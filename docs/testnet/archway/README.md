# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-2 | **Latest Version Tag**: v0.4.0 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ed7125298aa07ab9741dfe228dce937c3e53f396@185.52.52.26:26656,7d870183ad7e6ae3f441160530a2cd11896da522@46.4.5.45:11556,a05590886e3d3b0baa7a605ef2ee00db689308b8@35.238.216.151:26656,ec517b52edf929bc308fdef996054e11b5f00891@57.128.151.101:26656,073aa336bd5849677e40b199ab0266517fb5fe28@65.108.206.74:34656,7077f0635772fd56e9bfb704f9069694a42daf6b@148.113.6.190:25656,3320a6e7d7f1480e832d74d5ada53d8e275458bb@65.108.238.61:24656,85c669e01f5fca4d1ef7636a9526296a0083bb1d@15.235.193.57:26656,06aeab3dfcdbafba3db0010342b6e5596123e583@66.42.38.167:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
