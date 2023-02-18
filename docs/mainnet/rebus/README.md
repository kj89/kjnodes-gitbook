# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
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

**live-peers** (31)
```bash
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
