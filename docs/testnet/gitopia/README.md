# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


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

**live-peers** (34)
```
peers="ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,f3289c45d545c589a4114aeeb364fa4c6fde08d9@109.123.254.216:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,96fc6a8c3eb58d43c4ac41e9e642ba8485837ad3@109.123.255.116:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,42ba206efd9dd10847fa20f09a74fde6706442aa@194.146.13.128:60956,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,075aa5cd1437de2a072878c347f9d4eb5849c842@86.48.5.165:26656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,a8591524ebded3132f423771c0d91b77bdffad44@82.208.22.16:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,32245abf64927891bb1b6726c24a984d687ebbaf@38.242.153.36:41656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
