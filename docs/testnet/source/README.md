# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: [https://source-testnet.grpc.kjnodes.com](https://source-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ddb472d197b8a732bb3f8878035603769aa4c85b@161.35.75.82:26656,4466740c40895b6aad60a434f0ad3e3c5d5fe53c@213.239.216.252:22656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,071b2ba352b966e3af4f4fd0568beb923bf354d4@95.217.153.19:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,63d1b126558468634137b5705ab90151b16932f8@65.108.151.6:26656,1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,d0bf1f313c3fe5d9e890f7754950238493497211@62.171.178.217:26656,b958d18452ec5458323606d934906cc90d462203@194.233.93.124:26656,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
