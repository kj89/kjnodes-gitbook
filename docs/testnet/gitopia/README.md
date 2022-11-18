# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (21)
```
peers="0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,a47375da7f790427c69103d363e4f8de4a6acfac@5.199.143.159:36656,a5369601c7a7e44a5fdc893540d706c87a48a58c@185.197.251.195:41656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,6fa19dbe0236fc9328513ced95d9dd6f8330dbf3@34.160.118.165:26656,d2e951f1b808d95c4437762c452841fa400ec86f@139.59.33.196:26656,c630e7695e89074bf25a49afac7aca33feca9fd2@95.217.216.88:26656,1d3bb209dfc7fe953fb8fa37774bab34016dd75c@185.245.183.85:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,527c0753c83a5a89f5b51f50151b51a0d8638f7e@113.30.189.23:26656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,56c544dc2cf49daddc5958976ba01b8719a06200@65.21.178.237:656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,a08389b85b424dd5df4fb889ff1e6d32c692e325@65.21.227.78:30656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,9954c801a7019c5e4d7d762d4877866f7fd2a44e@176.9.106.43:36656,3a754aae8ee42a678b34a4393ff5bb658e43815e@137.184.165.200:41656,33e0b8b0abe1dd5f333544ecedd412a708dddd5f@34.162.241.115:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
