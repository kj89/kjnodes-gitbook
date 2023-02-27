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
peers="bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656,2475bcd6fc1950d8ddecfccd2c3161ce99130741@194.126.172.250:36656,c695376edc542f4324c57f6858a23cd701c1ae55@80.87.202.141:26656,3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,2e5ac443db5dc855bb33570ef58ce21cf130197f@82.208.21.15:36656,13eff3f60e60546435a9f79e241372b299f559a1@5.161.80.223:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
