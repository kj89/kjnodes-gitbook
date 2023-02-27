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

**live-peers** (9)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,08da04e20e295f48518d095871ba5c13e58c3dfd@185.209.223.64:36656,2475bcd6fc1950d8ddecfccd2c3161ce99130741@194.126.172.250:36656,2e5ac443db5dc855bb33570ef58ce21cf130197f@82.208.21.15:36656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,13eff3f60e60546435a9f79e241372b299f559a1@5.161.80.223:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
