# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

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

**live-peers** (10)
```bash
peers="dff203d0633c98eea4a228c5e913f22236043d89@23.88.69.101:16656,749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,117bf8ca700de022d9c87cd7cc7155958dc0ba23@185.188.249.18:02656,5b5438c8e0dbf7783c47b8cd41ca4eb8a4caa006@185.209.31.45:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
