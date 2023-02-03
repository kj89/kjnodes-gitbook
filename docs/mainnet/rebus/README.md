# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
