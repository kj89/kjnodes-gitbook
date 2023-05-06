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
peers="dda46cff53d11de64585e89cbe751671762c9ae9@176.9.28.41:26656,ec517b52edf929bc308fdef996054e11b5f00891@57.128.151.101:26656,da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,073aa336bd5849677e40b199ab0266517fb5fe28@65.108.206.74:34656,ed7125298aa07ab9741dfe228dce937c3e53f396@185.52.52.26:26656,986141f7be0203c442e4f13a97731a8c3449af1f@207.148.121.109:26656,06aeab3dfcdbafba3db0010342b6e5596123e583@66.42.38.167:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,92f4a62a35bf75c771709d94e39eb8fca2bd0059@54.36.227.1:26656,d18fba39ca91d2192f73e0af0cde2a49b130604e@95.217.144.107:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
