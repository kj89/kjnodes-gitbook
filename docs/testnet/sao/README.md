# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

SAO Network is a secure and decentralized Web3 storage infrastructure  based on Cosmos SDK and IPFS protocol. It aims to facilitate the adoption  of Web3 storage, support the growing demand for Web3 applications and  allow for a more decentralized way of storing and accessing data.

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Wasm**: OFF

[Website](https://www.sao.network) | [Discord](https://discord.gg/f4xzfvPhhA) | [Twitter](https://twitter.com/SAONetwork)




## Chain explorer
[https://explorer.kjnodes.com/sao-testnet](https://explorer.kjnodes.com/sao-testnet)

## Public endpoints

* api: [https://sao-testnet.api.kjnodes.com](https://sao-testnet.api.kjnodes.com)
* rpc: [https://sao-testnet.rpc.kjnodes.com](https://sao-testnet.rpc.kjnodes.com)
* grpc: [https://sao-testnet.grpc.kjnodes.com](https://sao-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@sao-testnet.rpc.kjnodes.com:49656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json
```

**live-peers** (20)
```bash
peers="4a4c330115ed36bf8a5c8ffbc568d165ee91bd72@207.154.243.48:20656,2aad459c0dd3a81b1d5eb297986c8d8309ad20e3@46.101.144.90:27656,266d8a31a1cecf8d2f673e4cb65ea736173428e9@165.22.76.250:20656,70502c3cbd5aabc12245f44bebf767d83fe76434@134.209.255.7:20656,5bf4920fac1647e12a24c0ae5af4b3ca19db2bb2@57.128.86.7:26656,ee0f6da4f64970738cdbb01d21c9ce5240c92ca4@157.245.150.110:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,72a2bbeb32621600de4b2a6ed42b11bf3be1105c@146.190.40.115:20656,04364210591838fa6ebdfd2ea59a6e4e5dbde1c3@159.223.77.250:20656,8167fbcc27bbf431f36b9a980c7ec57803502f2e@206.189.81.5:20656,22cb6793d2bc029121f9e1dffddeb6eae74a466c@178.128.24.92:20656,e5d450435d3041e57400edb1cb65845f33be5b13@167.71.53.182:26656,6597c93ed83a0b9860838be324959452462dae48@134.209.21.58:20656,a22a3ad8f847ab87bd64d0b9365b870750bde4e5@143.198.204.248:20656,395e1f7e7ea858fd9093de8832a25be67e7b6d9d@171.226.79.93:09656,d99276e75a528b1e5a40bee3fe41ffe80a3a5b1b@195.3.221.58:47656,bd38f8b14f549bc035eaf2f22e7832173f1fd761@198.199.74.16:20656,195af5406fabfcf1011056887d9afc82aee82f62@104.248.63.18:10656,7075469d8ed68a423e065b67bcde29b6ca4266fd@142.132.248.253:65528,557c49ddc6c98e5c5ac6030a93451ad5fcd54e34@164.90.147.133:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
