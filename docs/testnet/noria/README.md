# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/noria.png" alt=""><figcaption></figcaption></figure>

The Noria Network is the only stable-denominated  crypto network. It is envisioned to be the most  accessible and decentralized network for stable money.

**Chain ID**: oasis-3 | **Latest Version Tag**: v1.2.0 | **Wasm**: ON

[Website](https://noria.network) | [Discord](https://discord.gg/pseAWBQ6EZ) | [Twitter](https://twitter.com/NoriaNetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/noria-testnet](https://explorer.kjnodes.com/noria-testnet)

## Public endpoints

* api: [https://noria-testnet.api.kjnodes.com](https://noria-testnet.api.kjnodes.com)
* rpc: [https://noria-testnet.rpc.kjnodes.com](https://noria-testnet.rpc.kjnodes.com)
* grpc: noria-testnet.grpc.kjnodes.com:16190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@noria-testnet.rpc.kjnodes.com:16156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@noria-testnet.rpc.kjnodes.com:16159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/noria-testnet/addrbook.json > $HOME/.noria/config/addrbook.json
```

**live-peers** (23)
```bash
peers="73e5dc6e04a1dd28e5851191eb9dede07f0b38fb@141.94.99.87:14095,f60568a6ed1f848857c1c6c113719c1bb687c656@65.108.105.48:22156,8336e98410c1c9b91ef86f13a3254a2b30a1a263@65.108.226.183:22156,5eedd8cf7fefc037a6233b1991c2a3b653518560@65.108.230.113:31066,31df60c419e4e5ab122ca17d95419a654729cbb7@102.130.121.211:26656,216e01ba9863a27bfe5aecc2ab4d301448a6c6e8@51.79.103.100:26656,bb04cbb3b917efce76a8296a8411f211bad14352@159.203.5.100:26656,0fbeb25dfdae849be87d96a32050741a77983b13@34.87.180.66:26656,419438c7cb152a88a30d6922a2b2c7077dd4daf5@88.99.3.158:22156,60a15b1b7feb62b65d58cb4721340907c2092099@65.108.6.45:61656,b55e2db9b3b63fde77462c4f5ce589252c5f45af@51.91.30.173:2009,c818c3aa14ae8183578b7be0572c2dcd75613e72@186.233.185.214:26656,b2b8e67a3158e0854570c7de61812c8c6e92e4bc@65.108.206.118:61656,afe93314d3d1f3b0bdc20f213983bd902263e171@18.188.137.12:26656,4d8147a80c46ba21a8a276d55e6993353e03a734@165.22.42.220:26656,8dfca3c8a308fb6e682814ba5c33623dd346e572@65.109.23.114:22156,38de00b6d88286553eb123d16846190e5c594c59@51.79.30.118:26656,6b00a46b8c79deab378a8c1d5c2a63123b799e46@34.69.0.43:26656,846731f7097e684efdd6b9446d562228640e2b14@34.27.228.66:26656,e82fb793620a13e989be8b2521e94db988851c3c@165.227.113.152:26656,adb152a90a61b910feb4b2cdbd3f897251aa5452@116.202.227.117:16156,506b6d9ee2a697b7941d04c525faf18a17dc2dff@169.0.214.249:2010,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noria/config/config.toml
```
