# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (13)
```bash
peers="03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,790d36e7ea45d6660427d4c7473bac0ef525e78a@184.174.36.119:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
