# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (12)
```bash
peers="4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,2475bcd6fc1950d8ddecfccd2c3161ce99130741@194.126.172.250:36656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,69e89a5169fef99ed1b72dadd4f5c7b801616c88@142.132.209.236:21256,a583f951655a3c9934944d332bb4f6cf7416a3b7@94.131.108.126:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
